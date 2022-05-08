# Language
programming language i made that hasn't got a name yet.
currently deciding between Lax, Myth, Spark, Neo, Rush, Fleet, Wiz and Reflect

anyways, you will need masm32 for this to work, as it uses masm to assembly the asm file into an obj, and then links the obj into an exe. Yehahh could have been better? but it works fine so yaknow.

This langauge is converted into assembly before compilation. This is because you can add you're own assembly code alongside this language to build functions that would otherwise not be included, meaning you can do just about anything with it.

At the moment it just compiles files called code.txt cause idk what to name the file extention yet, ill add command line arguments whenever i can be bothered. (yeah ik it takes 2 seconds to do but im busy rn)

# --- Documentation ---

## -- functions --

functions are layed out as follows:

 #functionName(pa,rams){
 (tab indent)   code
                 moreCode
 }
 
 if a function has no paramiters then do:
 
 #functionName(null){
 }
 
 ## -- function calls --
 
 functions are called in the format: function argu ments
 example: StdOut message
 This would call StdOut and pass the varible message
 
 By default arguments passed to functions give the address to the varible for the function to use, not the value of the varible.
 If you have a function that needs the value, say a number, then use a '.' before the argument. For example:
 
 #inputstr(inputAddress){
    inputBytes = 100
    StdIn .inputBytes inputAddress
 }
 
 ## -- varibles --
 In this language all varibles are global, which im sure you will either love or hate.
 Varibles are deleared as you'd expect, example:
 
 varibleName = "hello"
 epicVarible = 1234
 
 For those of you that are able to code in asm, the varibles are directly translated into the .data section. This means you can add new lines n'stuff like you would in asm. Example:
 
 NewLine = "Today is sunny",10,0
 
 with 10 being a new line and 0 indicating the end of the string.
 
 BE AWARE: like i said above all varibles are global, meaning do not name two varibles the same name. To stop this happening in functions I've named all varibles definded within functions starting with the name of the function. So in the inputstr function varibles are named inputstrPrompt and inputstrAddress.
 
 ## -- embedded assembly --
 Embedding is possible because the code is translated into assembly basically directly.
 Embedding is done with a '/' followed by the asm code
 Example: /dec attempts
 
You most likely wont have to use this very often unless you are creating something new quite new, as most of the standered lib uses this to create functions that can be called, such as using assembly jumps to create for loops and string comparisons.

BE AWARE: when using the stack make sure you pop everything off that you added on before the end of the function. This is because the return address is stored at the topof the stack when the function is called, therefore anything you add on will be poped off at the end and used as the retirn address.

BE AWAREx2: When the return address is poped off it is saved into the esi register, so anything you have in there by the end of the functiuon will be replaced, not sure why you would be trying to transfer data between funtions using the esi register but keep a note anyway.

## -- Combining --
To combine with other code/lib's use 'combine', similer to import to include. 


## -- things im sorry about --
yeah so theres no joining strings, at least not yet. HOWEVER this can be inplemented by making you're own function, 
i'm thinking something like join stringaddr string1 string2  which would join theb strings and save the completed string into stringaddr.
Actually now i think about it thats pretty easy to do, ill do that at some point and add it into the standered lib.

Anyways for now you're gonna have to deal with doing:
#main(null){
    attempts = "0"
    attemptsOut = " Attempts made!",10,0
    StdOut attempts
    StdOut attemptsOut
    login
    /inc attempts
    main
}
