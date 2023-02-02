const viewMore = document.querySelectorAll('.dropdown');

viewMore.forEach(dropdown => {
    const viewInfo = dropdown.querySelector('.dish-more-info');
    const moreInfo = dropdown.querySelector('.hidden-dish-info-row');

    viewInfo.addEventListener('click', () => {
        moreInfo.classList.toggle('show-dish-info-row');
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