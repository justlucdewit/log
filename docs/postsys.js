const pageEl = document.getElementById("contentSpace");

function createPost(title, content){
    //create main post div
    const postEl = document.createElement("div");

    //create and append title
    const titleEl = document.createElement("h2");
    titleEl.innerText = title;
    postEl.appendChild(titleEl);

    for (const para of content){
        //create and append content
        const contentEl = document.createElement("h3");
        contentEl.innerHTML = para;
        postEl.appendChild(contentEl);
    }
    
    //create and append divider
    postEl.appendChild(document.createElement("hr"));


    //append main post div to page
    pageEl.appendChild(postEl)
}

fetch("./posts.json").then(res=>
    res.json()
).then((data)=>{
    for (const {title, paragraphs} of data){
        createPost(title, paragraphs);
    }
});