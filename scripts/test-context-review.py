import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('review',Path(__file__).with_name('context-review.py'))
review=importlib.util.module_from_spec(spec);spec.loader.exec_module(review)

class ReviewContract(unittest.TestCase):
    def test_known_loss_shapes_are_reviewed(self):
        cases=[('是余额不足吗', [{'kind':'question','observation_ids':[]}]),
               ('按你说的进行修改',[{'kind':'permission_scope','observation_ids':[]}]),
               ('优先处理批量 3 题以上卡住的问题',[{'kind':'task_requirement','observation_ids':['O1']}]),
               ('输出【优化处方】，图片由我自己插入',[{'kind':'task_requirement','observation_ids':['O1']}])]
        self.assertTrue(all(review.risk_reasons(text,units) for text,units in cases))

    def test_partition_keeps_all_high_risk_and_samples_rest(self):
        rows=[{'id':f'M{i:03}','risk_reasons':['constraint'] if i<3 else []} for i in range(12)]
        high,sentinel,remaining=review.select(rows)
        self.assertEqual(set(high),{'M000','M001','M002'})
        self.assertEqual(len(sentinel),2)
        self.assertEqual(set(high+sentinel+remaining),{r['id'] for r in rows})
        self.assertEqual(len(high+sentinel+remaining),len(set(high+sentinel+remaining)))
        self.assertEqual(review.select(list(reversed(rows)))[1],sentinel)

    def test_sentinel_gap_expands_to_all_remaining(self):
        plan={'targeted_ids':['M1','M2'],'sentinel':['M2'],'remaining':['M3','M4'],'whole_fallback':False}
        result={'messages':[{'id':i,'useful_requirements':1,'covered':0 if i=='M2' else 1,'partial':0,'missing':1 if i=='M2' else 0,'issues':[{'kind':'missing'}] if i=='M2' else []} for i in ['M1','M2']]}
        self.assertEqual(review.escalation(plan,result)['remaining_ids'],['M3','M4'])
        result['messages'][1].update(covered=1,missing=0,issues=[])
        self.assertFalse(review.escalation(plan,result)['remaining_review_required'])

    def test_incomplete_review_cannot_pass_as_clean(self):
        plan={'targeted_ids':['M1'],'sentinel':[],'remaining':[],'whole_fallback':False}
        with self.assertRaises(ValueError):review.escalation(plan,{'messages':[]})
        with self.assertRaises(ValueError):review.escalation(plan,{'messages':[{'id':'M1','useful_requirements':1,'covered':0,'partial':0,'missing':1,'issues':[]}]})

if __name__=='__main__':unittest.main()
