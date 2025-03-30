document.addEventListener("DOMContentLoaded", function(){
    const searchInput = document.getElementById('search-input');
    const resultsList = document.getElementById('results-list');
  
    searchInput.addEventListener('input', function(){
      const query = searchInput.value;
      // Only search if the query is longer than 2 characters
      if(query.length > 2){
        fetch(`/api/search?q=${encodeURIComponent(query)}`)
          .then(response => response.json())
          .then(data => {
            resultsList.innerHTML = '';

            data.forEach(item => {
              const li = document.createElement('li');
              li.className = 'flex justify-between gap-x-6 py-4';
              li.innerHTML = `
                <div class="flex min-w-0 gap-x-4">
                  <img class="w-12 h-12 flex-none rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="${item.name}">
                  <div class="min-w-0 flex-auto">
                    <p class="text-sm font-semibold text-gray-900">${item.first_name} ${item.last_name}</p>
                    <p class="mt-1 truncate text-xs text-gray-500">${item.email}</p>
                  </div>
                </div>
                <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                  <p class="text-sm text-gray-900">${item.job_title}</p>
                  <p class="mt-1 text-xs text-gray-500">${item.date_of_birth}</p>
                </div>
              `;
              resultsList.appendChild(li);
            });
          })
          .catch(error => console.error('Error fetching search results:', error));
      } else {
        resultsList.innerHTML = '';
      }
    });
  });
  