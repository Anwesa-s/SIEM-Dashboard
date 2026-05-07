export default function AlertsPanel({ alerts }) {

  return (
    <div>
      <h2>Alerts</h2>

      {alerts.length === 0 ? (
        <p>No alerts</p>
      ) : (
        alerts.map((alert, index) => (
          <div
            key={index}
            style={{
              border: "2px solid red",
              padding: "10px",
              marginBottom: "10px"
            }}
          >
            <h3>{alert.type}</h3>
            <p>{alert.message}</p>
            <p>Severity: {alert.severity}</p>
          </div>
        ))
      )}
    </div>
  );
}