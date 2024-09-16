import sys
sys.path.append("..")

import vmdit_retrieval
import vmdit_llm
import vmdit_trim
import vmdit_rewrite
import run_baseline_lm





def main():
    data_path = '../../data/eval_data/popqa/popqa1.jsonl'
    rewrite_path = 'new_query/popqa_q_1.jsonl'
    rel_path = 'relation_context/L2/relation_context_popqa_1.json'
    new_popqa_path= 'new_query/popqa1_n.jsonl'
    trimed_path= "trimmed_evidences/L2/trimmed_evidences_popqa_1.json"

    #vmdit_llm.f_main(data_path, rel_path)

    #vmdit_rewrite.f_main(data_path,rewrite_path)
    vmdit_retrieval.main(data_path, rewrite_path)

    vmdit_trim.f_main(rel_path, new_popqa_path, trimed_path)

    run_baseline_lm.main(trimed_path)


if __name__=='__main__':
    main()
