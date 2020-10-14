const generateMatrix = n => {
    const matrix = [];
    for (let i=0; i<n; i++) {
        const  row = [];
        for (let j=0; j<n; j++) {
            row.push(Math.random())
        }
        matrix.push(row)
    }
    return matrix;
}

const timeit = (func, args) => {
    const t0 = performance.now();
    const res = func(args);
    const t1 = performance.now()
    console.log("Call took " + (t1 - t0) + " milliseconds.")
}

const rowMajorTraverse = m => {
    let res = 0;
    for (let i=0; i<m.length; i++)
    for (let j=0; j<m.length;j++)
    if (m[i][j]>=0.5) res += 1;
    return res;
}

const columnMajorTraverse = m => {
    let res = 0;
    for (let i=0; i<m.length; i++)
    for (let j=0; j<m.length;j++)
    if (m[j][i]>=0.5) res += 1;
    return res;
}


let matrix = generateMatrix(10000)
timeit(columnMajorTraverse, matrix)
timeit(rowMajorTraverse, matrix)
