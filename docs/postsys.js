let pageEl = document.getElementById("contentSpace");

function createPost(title, content){
    //create main post div
    let postEl = document.createElement("div");

    //create and append title
    let titleEl = document.createElement("h2");
    titleEl.innerText = title;
    postEl.appendChild(titleEl);

    for (para of content){
        //create and append content
        let contentEl = document.createElement("h3");
        contentEl.innerHTML = para;
        postEl.appendChild(contentEl);
    }
    
    //create and append divider
    postEl.appendChild(document.createElement("hr"));


    //append main post div to page
    pageEl.appendChild(postEl)
}

fetch("./posts.json").then((resp)=>{
    return resp.json();
}).then((data)=>{
    for (const post of data){
        createPost(post["title"], post["paragraphs"])
    }
});