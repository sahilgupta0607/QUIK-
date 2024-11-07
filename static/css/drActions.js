    // Get modal elements
    const addProjectBtn = document.getElementById('addProjectBtn');
    const modalOverlay = document.getElementById('modalOverlay');
    const closeModal = document.getElementById('closeModal');
    const projectForm = document.getElementById('projectForm');
    const successMessage = document.getElementById('successMessage');

    // Hide modal by default on page load
    modalOverlay.style.display = 'none';

    // Function to open modal when clicking "Add Project"
    addProjectBtn.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent default link behavior
        modalOverlay.style.display = 'flex'; // Show the modal overlay
    });

    // Function to close modal when clicking the close button (cross)
    closeModal.addEventListener('click', () => {
        modalOverlay.style.display = 'none'; // Hide the modal overlay
    });

    // Function to close modal when clicking outside the modal content
    window.addEventListener('click', (event) => {
        if (event.target === modalOverlay) {
            modalOverlay.style.display = 'none'; // Hide the modal overlay
        }
    });

    // Handle form submission
    projectForm.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevent actual form submission

        // Show the success message
        successMessage.style.display = 'block';
        successMessage.style.opacity = '1'; // Set full opacity for the message initially

        // Fade out effect
        setTimeout(() => {
            successMessage.style.transition = 'opacity 1s ease-out';
            successMessage.style.opacity = '0'; // Gradually fade out the message
        }, 2000); // Wait for 2 seconds before starting the fade out

        // Hide the modal after submission
        modalOverlay.style.display = 'none';

        // Reset the form
        projectForm.reset();
    });


// Get modal elements for forum functionality
const requestForumBtn = document.getElementById('requestForumBtn');
const forumModalOverlay = document.getElementById('forumModalOverlay');
const closeForumModal = document.getElementById('closeForumModal');
const forumForm = document.getElementById('forumForm');
const forumSuccessMessage = document.createElement('div');

// Set up success message for forum form
forumSuccessMessage.id = 'forumSuccessMessage';
forumSuccessMessage.className = 'success-message';
forumSuccessMessage.innerHTML = '<i>&#10004;</i> Forum Request Submitted Successfully!';
forumSuccessMessage.style.display = 'none';
document.body.appendChild(forumSuccessMessage);

// Hide forum modal overlay by default
forumModalOverlay.style.display = 'none';

// Function to open forum modal on clicking "Request For Forum"
requestForumBtn.addEventListener('click', (e) => {
    e.preventDefault();
    forumModalOverlay.style.display = 'flex';
});

// Function to close forum modal on clicking close button
closeForumModal.addEventListener('click', () => {
    forumModalOverlay.style.display = 'none';
});

// Function to close forum modal if clicking outside the content area
window.addEventListener('click', (event) => {
    if (event.target === forumModalOverlay) {
        forumModalOverlay.style.display = 'none';
    }
});

// Handle forum form submission
forumForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Show the forum success message
    forumSuccessMessage.style.display = 'block';
    forumSuccessMessage.style.opacity = '1';

    // Fade out effect for forum success message
    setTimeout(() => {
        forumSuccessMessage.style.transition = 'opacity 1s ease-out';
        forumSuccessMessage.style.opacity = '0';
    }, 2000);

    // Hide the forum modal after submission
    forumModalOverlay.style.display = 'none';

    // Reset the forum form
    forumForm.reset();
});
