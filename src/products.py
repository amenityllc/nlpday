import spacy
import pandas as pd


def main(file_name):
    """
    Main method - reads sentences from CSV file, analyze sentences, run NLP rules for extraction and output results
    :param file_name: CSV file name with sentences
    :return: void
    """
    sentences = read_sentences(file_name)
    docs = analyze_sentences_spacy(sentences)

    for sentence, doc in zip(sentences, docs):
        print_analyzed_sentence(doc, sentence)

    extractions = []
    for sentence, doc in zip(sentences, docs):
        extractions += extract_new_products(sentence, doc)

    output_extractions(extractions)


def analyze_sentences_spacy(sentences):
    """
    Method analyzes sentences with SpaCy's NLP library
    :param sentences: iterable of sentences
    :return:  list of analyzed sentences
    """
    nlp = spacy.load('en_core_web_sm')
    return [nlp(sentence) for sentence in sentences]


def output_extractions(extractions):
    """
    Ouput extractions to CSV file
    :param extractions: list of list of (sentence, company, product)
    :return: void
    """
    df = pd.DataFrame(data=extractions, columns=['Sentence', 'Company', 'Product'])
    df.to_csv('extractions.csv', index=False)


def extract_new_products(sentence, doc):
    """
    Method gets a sentences and analyzed sentences and extracts triples of (sentence, company, product)
    :param sentence: original sentence
    :param doc: analyzed sentence
    :return: list of triples of (sentence, company, product)
    """
    extractions = []

    # TODO: implement

    return []


def build_extraction(sentence, company_name, product):
    return [sentence, company_name, product]


def print_analyzed_sentence(doc, sentence):
    """
    Helper method for printing analyzed sentences
    :param doc: NLP analyzed sentence
    :param sentence: original sentence
    :return: void
    """
    print(sentence + '\n')

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.ent_type_, token.head.text, token.head.pos_,
              [child for child in token.children])

    print()


def read_sentences(file_name):
    """
    Method reads sentences from a CSV file with a column names 'sentences'
    :param file_name:
    :return: list of string
    """
    data = pd.read_csv(file_name)
    sentences = list(data.sentence)
    return sentences


if __name__ == "__main__":
    main('data_with_articles.csv')
