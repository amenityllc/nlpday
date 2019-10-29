import random
import argparse
import pandas as pd


def augment_data(input_file: str, output_file: str):
    sentences_df = pd.read_csv(input_file)

    all_companies = set(sentences_df['company'].to_list())
    all_products = set(sentences_df['product'].to_list())

    new_rows = []
    for _, row in sentences_df.iterrows():

        # how many times to duplicate each row
        for _ in range(10):

            # replace the company and the product
            random_company = str(random.choice(tuple(all_companies)))
            random_product = str(random.choice(tuple(all_products)))
            sentence = row['sentence'].replace(str(row['company']), random_company).\
                replace(str(row['product']), random_product)

            new_rows.append([sentence, random_company, random_product])

    random.shuffle(new_rows)

    new_rows_df = pd.DataFrame(columns=['sentence', 'company', 'product'], data=new_rows)

    with open(output_file, 'w+') as out_fp:
        new_rows_df.to_csv(out_fp, index=False)


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--input-file", type=str, help='Input CSV', required=True)
    argument_parser.add_argument("--output-file", type=str, help='Output file', required=True)
    args = argument_parser.parse_args()
    augment_data(args.input_file, args.output_file)


if __name__ == '__main__':
    main()
