class ErrorListener():
    def __init__(self) -> None:
        self.true = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error in: {line} : {column} > {msg}")
        self.true = True

    def reportAmbiguity(
        self,
        recognizer,
        dfa,
        startIndex,
        stopIndex,
        exact,
        ambigAlts,
        configs
    ):
        pass

    def reportAttemptingFullContext(
        self,
        recognizer,
        dfa,
        startIndex,
        stopIndex,
        conflictingAlts,
        configs
    ):
        pass

    def reportContextSensitivity(
        self,
        recognizer,
        dfa,
        startIndex,
        stopIndex,
        prediction,
        configs
    ):
        pass
