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

// Highlight menu category on scroll
const menuCategories = document.querySelectorAll('.dish-cards-category');
const categoryNav = document.querySelectorAll('.menu-category');
const menuList = document.querySelector('#menu-list');
const SCROLL_PADDING_TOP = 65;
const SCROLL_MARGIN_ERROR = 15;
window.onscroll = () => {
    var current = "";

    menuCategories.forEach((category) => {
        if (window.pageYOffset >= (category.offsetTop - SCROLL_PADDING_TOP)) {
            current = category.getAttribute("id");
        }

    });

    categoryNav.forEach((a) => {
        console.log(window.pageYOffset, (menuList.offsetTop - SCROLL_PADDING_TOP), current)
        a.classList.remove("active");
        if (window.pageYOffset > (menuList.offsetTop - SCROLL_PADDING_TOP + SCROLL_MARGIN_ERROR) && a.innerText.includes(current)) {
            a.classList.add("active");
        }
    });
};

// Toggle show/hide for collapsible headings
const collapsibleHeadings = document.querySelectorAll('.heading-collapsible');
collapsibleHeadings.forEach(heading => {
    let content = heading.nextElementSibling;
    if (content) {
        heading.addEventListener('click', () => {
            heading.classList.toggle("active");
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }

        });
    }
})

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