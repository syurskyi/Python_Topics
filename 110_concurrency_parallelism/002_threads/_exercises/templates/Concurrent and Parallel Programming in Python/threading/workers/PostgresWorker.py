_______ os
_______ _______

____ q__ _______ Empty

____ sqlalchemy _______ create_engine
____ sqlalchemy.sql _______ text


c_ PostgresMasterScheduler(_______.T...
    ___  -  input_queue, $$
        __ 'output_queue' __ kwargs:
            kwargs.pop('output_queue')
        s__(PostgresMasterScheduler,   - (**kwargs)
        _input_queue = input_queue
        s..

    ___ run
        w.... T..:
            ___
                val = _input_queue.g..timeout=10)
            ______ Empty:
                print('Timeout reached in postgres scheduler, stopping')
                ______

            __ val == 'DONE':
                ______

            symbol, price, extracted_time = val
            postgresWorker = PostgresWorker(symbol, price, extracted_time)
            postgresWorker.insert_into_db()


c_ PostgresWorkerg___
    ___  -  symbol, price, extracted_time
        _symbol = symbol
        _price = price
        _extracted_time = extracted_time

        _PG_USER = os.environ.g..'PG_USER')
        _PG_PW = os.environ.g..'PG_PW')
        _PG_HOST = os.environ.g..'PG_HOST')
        _PG_DB = os.environ.g..'PG_DB')

        _engine = create_engine(f'postgresql://{_PG_USER}:{_PG_PW}@{_PG_HOST}/{_PG_DB}')

    ___ _create_insert_query
        SQL = """INSERT INTO prices (symbol, price, extracted_time) VALUES 
        (:symbol, :price, :extracted_time)"""
        r_ SQL

    ___ insert_into_db
        insert_query = _create_insert_query()

        w___ _engine.connect() __ conn:
            conn.execute(text(insert_query), {'symbol': _symbol,
                                              'price': _price,
                                              'extracted_time': str(_extracted_time)})
