
function addSubtask() {
    var subtaskContainer = document.getElementById('subtask-container');
    var newSubtaskDiv = document.createElement('div');

    newSubtaskDiv.innerHTML = `
        <br>
        <label for="subtask">Subtask:</label>
        <input type="text" name="subtasks[]" required>

        <br>

        <label for="subtask_time">Time to Complete:</label>
        <input type="text" name="subtask_times[]" pattern="([01]?[0-9]|2[0-3]):[0-5][0-9]" title="Enter a valid time in HH:MM format" required>

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
