_______ t___
_______ os

____ yaml_reader _______ YamlPipelineExecutor


___ main():
    pipeline_location = os.environ.get('PIPELINE_LOCATION')
    __ pipeline_location is None:
        print('Pipeline location not defined')
        exit(1)
    scraper_start_time = t___.t___()

    yamlPipelineExecutor = YamlPipelineExecutor(pipeline_location=pipeline_location)
    yamlPipelineExecutor.s..
    yamlPipelineExecutor.j...
    print('Extracting time took:', round(t___.t___() - scraper_start_time, 1))


__ __name__ == "__main__":
    main()
