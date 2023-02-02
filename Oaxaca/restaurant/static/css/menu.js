//Fetches the class dropdown which will be used to loop through to find every definition under it
const viewMore = document.querySelectorAll('.dish-info-dropdown');

viewMore.forEach(dropdown => {
    //Assigned the information to be shown as moreInfo
    const moreInfo = dropdown.querySelector('.dish-info-row');
    //Assigned the text of the button as button
    const button = dropdown.querySelector('.dish-info-dropdown-btn')

    //Created a functionality that understands whenever the dropdown button is pressed
    button.addEventListener('click', () => {
        button.classList.toggle("view-less");
        moreInfo.classList.toggle("show");
    });
});

// Functionality for each dish card (-) and (+) buttons
const dishOrderSubBtns = document.querySelectorAll('.dish-count-sub');
const dishOrderAddBtns = document.querySelectorAll('.dish-count-add');
const MIN_ORDER_COUNT = 1;
const MAX_ORDER_COUNT = 10;
dishOrderSubBtns.forEach(subBtn => {
    let dishCountInput = subBtn.nextElementSibling;
    if (dishCountInput) {
        subBtn.addEventListener('click', () => {
            if (dishCountInput.value > MIN_ORDER_COUNT) {
                dishCountInput.value = parseInt(dishCountInput.value) - 1;
            }
        });
    }
});
dishOrderAddBtns.forEach(addBtn => {
    let dishCountInput = addBtn.previousElementSibling;
    if (dishCountInput) {
        addBtn.addEventListener('click', () => {
            if (dishCountInput.value < MAX_ORDER_COUNT) {
                dishCountInput.value = parseInt(dishCountInput.value) + 1;
            }
        });
    }
});

// Function for filtering menu items in menu
function filterMenu() {
    console.log("filter")
}

//
function filterMenuGetChecked() {

}

// Function for filtering menu items with filter checkboxes
function filterMenuCheckbox() {

}

// Function for fitering menu items with search
function filterMenuSearch(query) {

}