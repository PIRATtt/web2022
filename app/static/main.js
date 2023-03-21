$('#delete-user-modal').on('show.bs.modal', function (event) {
    let url = event.relatedTarget.dataset.url;
    let form = this.querySelector('form');
    form.action = url;
    let username = event.target.closest('td').querySelector('.user-name').textContent;
    this.querySelector('#user-name').textContent = username;
  })