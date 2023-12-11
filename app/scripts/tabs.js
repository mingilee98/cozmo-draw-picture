function showTab(tabIndex) {
    var tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(function (tabContent) {
        tabContent.style.display = 'none';
    });

    var tabs = document.querySelectorAll('.tab');
    tabs.forEach(function (tab) {
        tab.classList.remove('active');
    });

    var selectedTabContent = document.getElementById('tabContent' + tabIndex);
    if (selectedTabContent) {
        selectedTabContent.style.display = 'block';
    }

    var selectedTab = document.querySelector('.tab:nth-child(' + (tabIndex + 1) + ')');
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
}
