import React, { useEffect, useState } from 'react';

function App() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/employees")
      .then((res) => {
        if (!res.ok) throw new Error("Erreur lors du fetch");
        return res.json();
      })
      .then((data) => {
        console.log("Employés :", data);
        setEmployees(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Erreur fetch :", err.message);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h1>Liste des employés</h1>

      {loading && <p>Chargement...</p>}
      {error && <p style={{ color: "red" }}>Erreur : {error}</p>}

      {!loading && !error && (
        <ul>
          {employees.length === 0 ? (
            <li>Aucun employé trouvé</li>
          ) : (
            employees.map((emp) => (
              <li key={emp.id}>
                <h3>{emp.name}</h3>
                <h5>{emp.role}</h5>
              </li>
            ))
          )}
        </ul>
      )}
    </div>
  );
}

export default App;
