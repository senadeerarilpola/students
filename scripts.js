const studentForm = document.getElementById('student-form');
const studentList = document.getElementById('student-list');

studentForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const grade = document.getElementById('grade').value;

    const studentDiv = document.createElement('div');
    studentDiv.textContent = `Name: ${name}, Age: ${age}, Grade: ${grade}`;
    studentList.appendChild(studentDiv);

    studentForm.reset();
});