alert('fart')

async function allCakes() {
    const res = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    
    for (let item of res.data.cakes)
    console.log(item.flavor)
}

allCakes()