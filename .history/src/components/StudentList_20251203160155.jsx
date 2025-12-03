function StudentList({students}){
    return(
        <div> 
            <h1>Student List</h1>
            {students.length === 0 ?(
                <p> No Studnet Added yet</p>
            ):
            (
                students.map(s, index) => (
                    <div key={index} className="studnet-card">
                        <strong>Name:</strong>{s.name}
                        
                    </div>
                )
            )
        };

        </div>
    )
}