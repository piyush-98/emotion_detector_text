data_card={
    "type": "text classification",
    "file_format": "pickled dataframe",
    "sources":{
        "name":"{CARER}: Contextualized Affect Representations for Emotion Recognition",
        "Url":"https://github.com/dair-ai/emotion_dataset",
    },
    "citations":
    r'''@inproceedings{saravia-etal-2018-carer,
    title = {CARER}: Contextualized Affect Representations for Emotion Recognition",
    author = "Saravia, Elvis  and
      Liu, Hsien-Chi Toby  and
      Huang, Yen-Hao  and
      Wu, Junlin  and
      Chen, Yi-Shin",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D18-1404",
    doi = "10.18653/v1/D18-1404",
    pages = "3687--3697",
    abstract = "Emotions are expressed in nuanced ways, which varies by collective or individual experiences, knowledge, and beliefs. Therefore, to understand emotion, as conveyed through text, a robust mechanism capable of capturing and modeling different linguistic nuances and phenomena is needed. We propose a semi-supervised, graph-based algorithm to produce rich structural descriptors which serve as the building blocks for constructing contextualized affect representations from text. The pattern-based representations are further enriched with word embeddings and evaluated through several emotion recognition tasks. Our experimental results demonstrate that the proposed method outperforms state-of-the-art techniques on emotion recognition tasks.",
''',
    "file_location":"https://git.unbiased.cc/unbiased-intelligence-hub/emotion_detector_text/-/tree/master/Data",
    "use_cases": "Emotion recognition from text",
    "file_columns": ["text","emotion"],
    "file_size":"47.6 MB",
    "total_data_samples":"416809",
    "labels":['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'],
    "data_distribution":{
        'joy':'141067',
        'sadness':'121187',
        'anger':'57317',
        'fear':'47712',
        'love':'34554',
        'surprise':'14972',
    }
}
import json
with open('data_card.json', 'w') as fp:
    json.dump(data_card, fp)