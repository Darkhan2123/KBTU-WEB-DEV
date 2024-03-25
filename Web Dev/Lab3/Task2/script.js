document.getElementById("button").addEventListener("click", function(){
    let task = document.getElementById("input").value;

    if(task){
        let taskBox = document.createElement("div");
        taskBox.classList.add("task-box");

        let checkBox = document.createElement("input");
        checkBox.type = "checkbox";
        checkBox.classList.add("task-checkbox");
        taskBox.appendChild(checkBox);

        let taskText = document.createElement("span");
        taskText.textContent = task;
        taskBox.appendChild(taskText);

        let deleteButton = document.createElement("button");
        deleteButton.textContent = "🗑️"
        deleteButton.classList.add("delete-button");
        taskBox.appendChild(deleteButton);

        document.querySelector(".list").appendChild(taskBox);
        document.getElementById("input").value = "";
    }
})

document.querySelector(".list").addEventListener("change", function(e) {
    if (e.target.classList.contains("task-checkbox")) {
        e.target.nextSibling.style.textDecoration = e.target.checked ? "line-through" : "none";
    }
});

document.querySelector(".list").addEventListener("click", function(e) {
    if (e.target.classList.contains("delete-button")) {
        e.target.parentElement.remove();
    }
});

