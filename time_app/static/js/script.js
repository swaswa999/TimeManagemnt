
function addSubtask() {
    var subtaskContainer = document.getElementById('subtask-container');
    var newSubtaskDiv = document.createElement('div');

    newSubtaskDiv.innerHTML = `
        <br>
        <label for="subtask">Subtask:</label>
        <input type="text" name="subtasks[]" required>

        <br>

        <label for="subtask_time">When to Complete by:</label>
        <input type="date" name="due_date[]">
        <br>
        <br>

        <button type="button" onclick="removeSubtask(this)">Remove</button>

        <br>
    `;

    subtaskContainer.appendChild(newSubtaskDiv);
}

// JavaScript function to remove a subtask input field
function removeSubtask(buttonElement) {
    var subtaskContainer = document.getElementById('subtask-container');
    var subtaskDiv = buttonElement.parentElement;
    subtaskContainer.removeChild(subtaskDiv);
}

var isDueDateVisible = false;

function addDate() {
    var repeatNoContainer = document.getElementById('repeat_no').parentElement;
    var dueDateContainer = repeatNoContainer.querySelector('.due-date-container');

    if (isDueDateVisible) {
        // If the due date is visible, hide it
        repeatNoContainer.removeChild(dueDateContainer);
    } else {
        // If the due date is not visible, show it
        dueDateContainer = document.createElement('div');
        dueDateContainer.classList.add('due-date-container'); // Add a class for identification

        dueDateContainer.innerHTML = `
            <label for="due_date">Due Date:</label>
            <input type="date" id="due_date" name="due_date" required>
            <br> 
        `;

        repeatNoContainer.appendChild(dueDateContainer);
    }

    // Toggle the flag
    isDueDateVisible = !isDueDateVisible;
}
