
class CompletionHalt {
    reason string @description(#"
        The reason completion is being halted, 
        e.g. 'Response finished satisfactorily'
        or
        'Out of remaining words.'
    "#)
} // 

class InitBlock {
    prompt string
    limit int @description(#"
        Words left in total response.
    "#)
} // InitBlock


class ContextBlock {
    prompt string
    limit int @description(#"
        Words left in total response.
    "#)
    generated string @description(#"
        Text generated thus far.
    "#)
} // ContextBlock

class Response {
    word string @description(#"
        The best next word. Limit to 1 word.
    "#)
}

function InitOutput(init: InitBlock) -> Response {
    client "openai/gpt-4o-mini"
    prompt #"
        Based on {{ init }},
        {{ ctx.output_format }}
    "#
} // NextWork

function GeneralOutput(block: ContextBlock) -> Response {
    client "openai/gpt-4o-mini"
    prompt #"
        Based on {{ block }}
        {{ ctx.output_format }}
    "#
} // GeneralOutput

function Genesis(request: string, limit: int) -> Response {
    client "openai/gpt-4o-mini"
    prompt #"
        You are a completion tool that is trying to output an answer to the following prompt
        {{ request }}
        in {{ limit }} words at most. You are to generate the first word of the sentence (usually 'The')
        {{ ctx.output_format }}
    "#
}

function Output(request: string, limit: int, generated: string) -> Response | CompletionHalt {
    client "openai/gpt-4o-mini"
    prompt #"
        You are a completion tool, answering 
        BEGINREQUEST
        {{ request }}
        END REQUEST
        one word at a time, using proper capitalization and punctuation (even if the request has flawed grammar or punctuation), building on what has already been generated:
        BEGINQUOTE
        {{ generated }}
        ENDQUOTE
        You have {{ limit }} words remaining in the total answer. Remember that if the prev word ends in a period, the next word must begin a new sentence. Synthesize based on the request and answer thus far rather than summarizing them. Don't be repetitive in theme or style.
        {{ ctx.output_format }}
    "#
} // Output

test genesis {
    functions [Genesis] 
    args {
        request "Explain the role of the Pope in the Roman Catholic Church."
        limit 20
    }
}

test output {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 49
        generated "The"
    }
}

test output1 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 48
        generated "The Pope"
    }
}

test output2 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 47
        generated "The Pope serves"
    }
}

test output3 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 46
        generated "The Pope serves as"
    }
}


test output4 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 45
        generated "The Pope serves as the"
    }
}

test output5 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 44
        generated "The Pope serves as the leader"
    }
}

test output6 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 43
        generated "The Pope serves as the leader of"
    }
}

test output7 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 42
        generated "The Pope serves as the leader of the"
    }
}

test output8 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 41
        generated "The Pope serves as the leader of the Roman"
    }
}

test output9 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 40
        generated "The Pope serves as the leader of the Roman Catholic"
    }
}

test output10 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 39
        generated "The Pope serves as the leader of the Roman Catholic Church,"
    }
}

test output11 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 38
        generated "The Pope serves as the leader of the Roman Catholic Church, providing"
    }
}

test output12 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 37
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance."
    }
}

test output13 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 36
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance. His"
    }
}

test output14 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 35
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance. His authority"
    }
}

test output15 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 34
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance. His authority is"
    }
}

test output16 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 3
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance. His authority is"
    }
}

test output17 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 2
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance. His authority is spiritual"
    }
}

test output18 {
    functions [Output]
    args {
        request "Explain the role of the pope in the rc church"
        limit 1
        generated "The Pope serves as the leader of the Roman Catholic Church, providing guidance. His authority is spiritual and administrative."
    }
}