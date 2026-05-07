export default function EventTable({ events }) {
  return (
    <div>
      <h2>Security Events</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Source IP</th>
            <th>Type</th>
            <th>Severity</th>
            <th>Message</th>
          </tr>
        </thead>

        <tbody>
          {events.map((event) => (
            <tr key={event.id}>
              <td>{event.id}</td>
              <td>{event.source_ip}</td>
              <td>{event.event_type}</td>
              <td>{event.severity}</td>
              <td>{event.message}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}