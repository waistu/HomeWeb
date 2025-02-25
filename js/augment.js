function openPopup(popupId) {
    const popup = document.getElementById(popupId);
    popup.style.display = 'flex';
}

function closePopup(popupId) {
    const popup = document.getElementById(popupId);
    popup.style.display = 'none';
}

function stopPropagation(event) {
    event.stopPropagation();
}

function closePopupOutside(event) {
    if (event.target === event.currentTarget) {
        const popupId = event.currentTarget.id;
        closePopup(popupId);
    }
}

