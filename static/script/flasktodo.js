let editButtons = document.querySelectorAll('.edit-button');
editButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        let todoId = event.target.dataset.todoId;
        let todoTitle = document.getElementById('todo-title-' + todoId);
        let editInput = button.parentNode.querySelector('.edit-input');
        let saveButton = button.parentNode.querySelector('.save-button');
        
        // Hide the todo title and show the edit input field and save button
        todoTitle.style.display = 'none';
        editInput.style.display = 'block';
        saveButton.style.display = 'inline-block';

        // Add event listener for Escape key press
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                // Show the todo title and hide the edit input field and save button
                todoTitle.style.display = 'inline-block';
                editInput.style.display = 'none';
                saveButton.style.display = 'none';
            }
        });
    });
});        
