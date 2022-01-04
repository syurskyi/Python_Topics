____ true_or_false.game_result _______ GameResult
____ true_or_false.game_status _______ GameStatus
____ true_or_false.question _______ Question


c_ Game:

    ___ __parse_line(self, line):
        parts  line.s..(';')
        text  parts[0]
        is_correct  parts[1] __ "Yes"
        explanation  parts[2]

        r.. Question(text, is_correct, explanation)

    ___ __fill_in_questions(self, file_path, questions: []):
        w__ open(file_path, encoding'UTF8') __ file:
            ___ line __ file:
                q  __parse_line(line)
                questions.a..(q)

    ___ - , file_path, allowed_mistakes, end_of_game_callback):
        __file_path  file_path
        __allowed_mistakes  allowed_mistakes
        __end_of_game  end_of_game_callback
        __mistakes  0
        __questions  []
        __counter  0
        __game_status  GameStatus.IN_PROGRESS

        __fill_in_questions(file_path, __questions)

    ___ get_next_question
        r.. __questions[__counter]

    ___ give_answer(self, answer):
        ___ is_last_question
            r.. __counter __ l..(__questions) - 1

        ___ exceeded_allowed_mistakes
            r.. __mistakes > __allowed_mistakes

        __ __questions[__counter].is_true ! answer:
            __mistakes + 1

        __ is_last_question() o. exceeded_allowed_mistakes
            __game_status  GameStatus.GAME_IS_OVER

            result  GameResult(__counter, __mistakes, __mistakes < __allowed_mistakes)
            __end_of_game(result)

        __counter + 1

    $
    ___ game_status
        r.. __game_status
