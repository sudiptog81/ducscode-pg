import java.awt.*;
import java.awt.event.*;

public class Main extends Frame implements ActionListener {
  public Main() {
    setLayout(new FlowLayout());

    addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent evt) {
        System.exit(0);
      }
    });

    setTitle("AWT Counter");
    setSize(250, 100);
    setVisible(true);
  }

  public static void main(String[] args) {
    new Main();
  }

  @Override
  public void actionPerformed(ActionEvent evt) {
  }
}
