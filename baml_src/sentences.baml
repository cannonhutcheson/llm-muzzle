
class SentenceResponse {
    sentence string
} // SentenceResponse

class Punctuate {
    reason string? @description(#"
        Explanation of why the text is ending, e.g 'Not enough words remaining' or, in rare cases 'Sufficiently described'
    "#)
} // Punctuate

class Error {
    reason string? @description(#"
        An explanation of why an error is being thrown.
    "#)
}

function GenFirstSentence(request: string, limit: int) -> SentenceResponse | Error {

    client CustomGPT4oMini
    prompt #"
        You are a completion tool that is used to write the first sentence of a response to the following prompt:
        BEGINPROMPT
        {{ request }}
        ENDPROMPT
        Keeping in mind that the total answer (including subsequent sentences) must conform to a {{ limit }} word limit. Generate the first sentence.
        {{ ctx.output_format }}
    "#
} // GenFirstSentence

function GenNextSentence(request: string, limit: int, generated: string) -> SentenceResponse | Punctuate {
    client CustomGPT4oMini
    prompt #"
        You are a completions tool used to generate the next sentence or end the text in the following paragraph (note, we want to approach the word limit asymtotically. Meaning, if there are many more words left available, synthesize more):
        BEGINQUOTE
        {{ generated }}
        ENDQUOTE
        Which is being used to respond to the following prompt:
        BEGINQUOTE
        {{ request }}
        ENDQUOTE
        The remaining word limit is {{ limit }}
        {{ ctx.output_format }}
    "#
} // GenNextSentence

test first {
    functions [GenFirstSentence]
    args {
        request  #"
            Explain the role of the Pope in the Catholic Church.
        "#
        limit 50
    }
} // first

test second {
    functions [GenNextSentence]
    args {
        request  #"
            Explain the role of the Pope in the Catholic Church.
        "#
        limit 22
        generated #"
            The Pope serves as the spiritual leader of the Catholic Church, guiding its members in faith and doctrine while representing the Church in global religious and social matters.
        "#
        
    }
}

test third {
    functions [GenNextSentence]
    args {
        request  #"
            Explain the role of the Pope in the Catholic Church. 
        "#
        limit 6
        generated #"
            The Pope serves as the spiritual leader of the Catholic Church, guiding its members in faith and doctrine while representing the Church in global religious and social matters. Additionally, the Pope provides moral guidance, addresses social justice issues, and fosters ecumenical dialogue with other faiths.
        "#
    }
}
