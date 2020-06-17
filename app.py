import sys
from util import get_tables, load_db_details
from read import read_table


def main():
    env = sys.argv[1]
    db_details = load_db_details(env)
    tables = get_tables('table_list')
    for table in tables['table_name']:
        print(f'reading data for {table_name}')
        data, columns = read_table(db_details, table)
        print(f'loading data for {table_name}')



if __name__ == '__main__':
    main()