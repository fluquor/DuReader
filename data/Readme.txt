Here is an example of the data:

{
"question": "中国银监会云南监管局是否同意了中信银行昆明翠湖社区支行终止营业的请求吗？", 
"documents": 
[
{"bs_rank_pos": 1, 
"is_selected": true, 
"paragraphs": ["中国银监会云南监管局同意中信银行股份有限公司昆明翠湖社区支行终止营业。"], 
"title": "中国银监会云南监管局是否同意了中信银行昆明翠湖社区支行终止营业的请求吗？"
}
], 
"question_type": "yes_no", 
"yesno_answers": ["yes", "是"], 
"fact_or_opinion": "FACT", 
"answers": ["是"], 
"question_id": "spdb91"
}

"question_id" is the uniq id for each data example.
"question_type" provides 3 question types: "DESCRIPTION", "YES_NO", "ENTITY".
For each 'YES_NO' question,  there is a "yesno_answers" field which contains opinion types ("YES", "NO", "DEPENDS") to corresponding answers. 
For each 'ENTITY' question, there is an 'entity_answers' field containing a list of entity list, and each of the entity list contains named entities extracted from corresponding 'answer' sentences.
For all question types, "documents" field contains only one documents related to the question, and we segment the document into a  paragraph and store them in "paragraphs" field. And each document's title is stored in "title" field.
"is_selected" indicates whether the annotator referred to this document when summarizing the answers. If it is set to False, the annotator didn't choose this document as a reference.
"bs_rank_pos" indicates the rank of this document,it is default 0.
