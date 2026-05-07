import {
  PieChart,
  Pie,
  Tooltip,
  Cell
} from "recharts";

export default function SeverityChart({ events }) {

  const counts = {
    HIGH: 0,
    LOW: 0
  };

  events.forEach((e) => {
    if (e.severity === "HIGH") counts.HIGH++;
    else counts.LOW++;
  });

  const data = [
    { name: "HIGH", value: counts.HIGH },
    { name: "LOW", value: counts.LOW }
  ];

  return (
    <div>
      <h2>Severity Distribution</h2>

      <PieChart width={300} height={300}>
        <Pie
          data={data}
          dataKey="value"
          outerRadius={100}
          label
        >
          <Cell fill="#ff4d4d" />
          <Cell fill="#4da6ff" />
        </Pie>

        <Tooltip />
      </PieChart>
    </div>
  );
}