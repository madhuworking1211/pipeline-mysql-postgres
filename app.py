import sys
from util import get_tables, load_db_details
from read import read_table
from write import load_table,build_insert_query


def main():
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('table_list')
    for table in tables['table_name']:
        data, column_names = read_table(db_details, table)
        test = build_insert_query(table, column_names)
        load_table(db_details,data,column_names,table)
        print(f'Successfully completed process for {table}')


if __name__ == '__main__':
    main()