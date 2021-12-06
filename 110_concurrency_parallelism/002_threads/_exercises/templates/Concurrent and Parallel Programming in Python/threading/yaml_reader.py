_______ importlib
_______ _______
_______ t___

_______ yaml
____ multiprocessing _______ Queue


c_ YamlPipelineExecutor(_______.T...):
    ___  -  pipeline_location):
        s__(YamlPipelineExecutor,   - ()
        _pipline_location = pipeline_location
        _queues = {}
        _workers = {}
        _queue_consumers = {}
        _downstream_queues = {}

    ___ _load_pipeline
        w___ open(_pipline_location, 'r') __ inFile:
            _yaml_data = yaml.safe_load(inFile)

    ___ _initialize_queues
        ___ queue __ _yaml_data['queues']:
            queue_name = queue['name']
            _queues[queue_name] = Queue()

    ___ _initialize_workers
        ___ worker __ _yaml_data['workers']:
            WorkerClass = getattr(importlib.import_module(worker['location']), worker['class'])
            input_queue = worker.get('input_queue')
            output_queues = worker.get('output_queues')
            worker_name = worker['name']
            num_instances = worker.get('instances', 1)

            _downstream_queues[worker_name] = output_queues
            __ input_queue is not None:
                _queue_consumers[input_queue] = num_instances
            init_params = {
                'input_queue': _queues[input_queue] __ input_queue is not None ____ None,
                'output_queue': [_queues[o...] ___ output_queue __ output_queues] \
                    __ output_queues is not None ____ None
            }

            input_values = worker.get('input_values')
            __ input_values is not None:
                init_params['input_values'] = input_values

            _workers[worker_name] = []
            ___ i __ r..(num_instances):
                _workers[worker_name].a..(WorkerClass(**init_params))

    ___ _join_workers
        ___ worker_name __ _workers:
            ___ worker_thread __ _workers[worker_name]:
                worker_thread.j...

    ___ process_pipeline
        _load_pipeline()
        _initialize_queues()
        _initialize_workers()
        # self._join_workers()

    ___ run
        process_pipeline()

        w.... True:
            total_workers_alive = 0
            worker_stats = []
            to_del = []
            ___ worker_name __ _workers:
                total_worker_threads_alive = 0
                ___ worker_thread __ _workers[worker_name]:
                    __ worker_thread.is_aliveg___
                        total_worker_threads_alive += 1
                total_workers_alive += total_worker_threads_alive
                __ total_worker_threads_alive == 0:
                    __ _downstream_queues[worker_name] is not None:
                        ___ o... __ _downstream_queues[worker_name]:
                            number_of_consumers = _queue_consumers[o...]
                            ___ i __ r..(number_of_consumers):
                                _queues[o...].put('DONE')

                    to_del.a..(worker_name)

                worker_stats.a..([worker_name, total_worker_threads_alive])
            print(worker_stats)
            __ total_workers_alive == 0:
                ______

            # queue_stats = []
            # for queue in self._queues:
            #     queue_stats.append([queue, self._queues[queue].qsize()])
            #
            # print(queue_stats)

            ___ worker_name __ to_del:
                del _workers[worker_name]

            t___.s..(1)
