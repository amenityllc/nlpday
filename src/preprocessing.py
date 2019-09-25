import argparse
import json
from typing import List
import pandas as pd


def _contains_company_and_product(attributes: pd.Series) -> List[int]:
    indices = []
    for index, value in attributes.iteritems():
        attributes_json = json.loads(value)
        found_company = False
        found_product = False
        entities = attributes_json['entitiesInsideEvent'] + attributes_json['entitiesOutsideEvent']
        for entity in entities:
            if 'ORG' in entity.keys():
                found_company = True
            if 'PRODUCT' in entity.keys():
                found_product = True
        if found_product and found_company:
            indices.append(index)
    return indices


def filter_rows(input_file: str, output_file: str):
    sentences_df = pd.read_csv(input_file)
    valid_rows = _contains_company_and_product(sentences_df['attributes'])
    sentences_df = sentences_df.iloc[valid_rows, :]

    del sentences_df['attributes']

    with open(output_file, 'w+') as out_fp:
        sentences_df.to_csv(out_fp, index=False)


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--input-file", type=str, help='Input CSV', required=True)
    argument_parser.add_argument("--output-file", type=str, help='Output file', required=True)
    args = argument_parser.parse_args()
    filter_rows(args.input_file, args.output_file)


if __name__ == '__main__':
    main()
