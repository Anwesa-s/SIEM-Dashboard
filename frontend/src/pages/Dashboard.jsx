import { useEffect, useState } from "react";
import API from "../api";

import EventTable from "../components/EventTable";
import SeverityChart from "../components/SeverityChart";
import AlertsPanel from "../components/AlertsPanel";

export default function Dashboard() {

  const [events, setEvents] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {

    fetchEvents();
    fetchAlerts();

  }, []);

  const fetchEvents = async () => {
    const res = await API.get("/events");
    setEvents(res.data);
  };

  const fetchAlerts = async () => {
    const res = await API.get("/alerts");
    setAlerts(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>SIEM Dashboard</h1>

      <AlertsPanel alerts={alerts} />

      <SeverityChart events={events} />

      <EventTable events={events} />

    </div>
  );
}