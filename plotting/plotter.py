import matplotlib.pyplot as plt

class Plotter:
    """
    A class responsible for plotting training and validation losses in both real-time and post-training.
    """

    @staticmethod
    def plot_loss_vs_epochs(train_losses, val_losses=None):
        """
        Plot the training and validation losses after the training has completed.

        Args:
            train_losses (list): List of training losses per epoch.
            val_losses (list, optional): List of validation losses per epoch.
        """
        epochs = range(1, len(train_losses) + 1)
        plt.figure(figsize=(10, 6))

        # Plot training loss
        plt.plot(epochs, train_losses, label='Training Loss')

        # Plot validation loss if available
        if val_losses:
            plt.plot(epochs, val_losses, label='Validation Loss')

        plt.title('Training and Validation Loss vs Epochs')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_real_time(train_losses, val_losses, current_epoch):
        """
        Plot training and validation losses in real-time during the training process.

        Args:
            train_losses (list): List of training losses up to the current epoch.
            val_losses (list): List of validation losses up to the current epoch.
            current_epoch (int): The current epoch being processed.
        """
        plt.clf()  # Clear the current figure for real-time updates
        plt.title(f"Training and Validation Loss (Epoch {current_epoch})")
        plt.xlabel("Epochs")
        plt.ylabel("Loss")

        # Plot training loss
        plt.plot(range(1, len(train_losses) + 1), train_losses, label="Training Loss")

        # Plot validation loss if available
        if val_losses:
            plt.plot(range(1, len(val_losses) + 1), val_losses, label="Validation Loss")

        plt.legend()
        plt.pause(0.001)  # Pause to allow the plot to update in real time
