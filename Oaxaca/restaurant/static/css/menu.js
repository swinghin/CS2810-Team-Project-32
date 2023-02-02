//Fetches the class dropdown which will be used to loop through to find every definition under it
const viewMore = document.querySelectorAll('.dish-info-dropdown');

viewMore.forEach(dropdown => {
    //Assigned the information to be shown as moreInfo
    const moreInfo = dropdown.querySelector('.dish-info-row');
    //Assigned the text of the button as button
    const button = dropdown.querySelector('.dish-info-dropdown-btn')

    moreInfo.style.display = "none";

    //Created a functionality that understands whenever the dropdown button is pressed
    button.addEventListener('click', () => {
        button.classList.toggle("view-less");
        moreInfo.classList.toggle("show");
    });
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