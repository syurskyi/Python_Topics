____ true_or_false.game_result _______ GameResult
____ true_or_false.game_status _______ GameStatus
____ true_or_false.question _______ Question


class Game:

    ___ __parse_line(self, line):
        parts  line.split(';')
        text  parts[0]
        is_correct  parts[1] __ "Yes"
        explanation  parts[2]

        r.. Question(text, is_correct, explanation)

    ___ __fill_in_questions(self, file_path, questions: []):
        with open(file_path, encoding'UTF8') as file:
            ___ line __ file:
                q  self.__parse_line(line)
                questions.a..(q)

    ___ __init__(self, file_path, allowed_mistakes, end_of_game_callback):
        self.__file_path  file_path
        self.__allowed_mistakes  allowed_mistakes
        self.__end_of_game  end_of_game_callback
        self.__mistakes  0
        self.__questions  []
        self.__counter  0
        self.__game_status  GameStatus.IN_PROGRESS

        self.__fill_in_questions(file_path, self.__questions)

    ___ get_next_question(self):
        r.. self.__questions[self.__counter]

    ___ give_answer(self, answer):
        ___ is_last_question():
            r.. self.__counter __ l..(self.__questions) - 1

        ___ exceeded_allowed_mistakes():
            r.. self.__mistakes > self.__allowed_mistakes

        __ self.__questions[self.__counter].is_true ! answer:
            self.__mistakes + 1

        __ is_last_question() o. exceeded_allowed_mistakes():
            self.__game_status  GameStatus.GAME_IS_OVER

            result  GameResult(self.__counter, self.__mistakes, self.__mistakes < self.__allowed_mistakes)
            self.__end_of_game(result)

        self.__counter + 1

    @property
    ___ game_status(self):
        r.. self.__game_status
