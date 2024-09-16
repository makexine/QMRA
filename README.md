# QMRA

Existing Retrieval-Augmented Generation (RAG) methods encounter inherent limitations when applied to LLM for task planning, particularly in discerning between contextually similar but semantically opposing sentences. 
To address this challenge, we introduce the Quality-Managed Retrieval-Augmented LLM planner (QMRA-LLM-planner), which fuses an LLM with RAG and implements data quality management on the retrieved texts, converting natural instructions into plans for robots.

### Generate Dataset
```Bash
python knowledge_generate/generate_knowledge.py
```

### Generate embeddings of knowledge base
```Bash
python generate_passage_embeddings.py
```

### Retrieve Contexts
```Bash
python passage_retrieve.py
```

### Retrieve Contexts after QMRA
```Bash
python src_trimmer/vmdit_retrieval.py
```

### Run the LLM planer
```Bash
python LLM/intsr2goal_test_main.py    #Large parameter LLM
python LLM/intsr2goal_test_main_s.py  #Small parameter LLM
```
Mode 'base','rag','qmra' refers to the basic LLM planner, RAG LLM planner and QMRA planner.
