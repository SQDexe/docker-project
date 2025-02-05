/* https://stackoverflow.com/questions/32589197/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string-using-javascript */
export const capitalise = str =>
    str.toLowerCase()
        .split(' ')
        .map(x => x.charAt(0).toUpperCase() + x.slice(1))
        .join(' '); 