_______ time
_______ os

from yaml_reader _______ YamlPipelineExecutor


___ main():
    pipeline_location = os.environ.get('PIPELINE_LOCATION')
    __ pipeline_location is None:
        print('Pipeline location not defined')
        exit(1)
    scraper_start_time = time.time()

    yamlPipelineExecutor = YamlPipelineExecutor(pipeline_location=pipeline_location)
    yamlPipelineExecutor.start()
    yamlPipelineExecutor.join()
    print('Extracting time took:', round(time.time() - scraper_start_time, 1))


__ __name__ == "__main__":
    main()
