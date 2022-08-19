import "./App.css";
import Home from "./pages/Home";
import AppRouter from "./router/AppRouter";

function App() {
  return (
    <div>
      <AppRouter>
        <Home />
      </AppRouter>
    </div>
  );
}

export default App;
