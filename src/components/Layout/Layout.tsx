
import HeaderWithSidebar from "../HeaderAndSideBar/HeaderWithSidebar";
import { Outlet } from "react-router-dom";
import classes from "./Layout.module.css";
import { Box } from "@chakra-ui/react";

function Layout() {
  return (
    <main className={classes.mainLayout}>
      <section className={classes.headerRow}>
        <div className={classes.mainHeader}>
          <HeaderWithSidebar />
        </div>
      </section>

      <section className={classes.mainContent}>
          <Outlet />
      </section>

      <section className={classes.footerRow}>
        <div className={classes.mainFooter}>
          <footer><Box backgroundColor={"#22224C"}> oi </Box></footer>
        </div>
      </section>
    </main>
  );
}

export default Layout;
