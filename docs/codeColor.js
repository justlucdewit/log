//color definitions
let color = [18, 29, 227];

//gather codeblocks
console.log("codeColor online")
let codeblocks = document.getElementsByClassName("code");

for (codeblock in codeblocks){
	//give everything the base color
	console.log(codeblocks[codeblock].style.color)
}