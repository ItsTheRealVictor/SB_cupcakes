alert('fart')

function makeHTML(cake){
    // copied this right out of the home.html jinja loop
    return `
    <div class="col-4">
    
        <div class="card my-2">
            <div class="card-body">
                <h5 class="card-title">${cake.flavor}</h5>
                <h6 class="card-subtitle text-muted">Rating: ${cake.rating}</h6>
                <h6 class="card-subtitle text-muted my-2">Size: ${cake.size}</h6>
                <img class="card-img-top" src="${cake.image}" alt="">
                <form style="display:inline" action="/delete/${cake.id}" method="POST">
                    <button class="btn btn-sm btn-danger">DELETE CAKE</button>
                </form>
    
            </div>
        </div>
    </div>
    `
}


async function allCakes() {
    const res = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    
    
    for (let cake of res.data.cakes){

        let newCake = $(makeHTML(cake));
        $('#cake-row').append(newCake)
        console.log(cake.flavor)

    }
}
allCakes()