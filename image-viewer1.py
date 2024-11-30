class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ImageViewer:
    def __init__(self):
        self.head = None
        self.current = None
    
    #adding image paths to the file 
    def add_image(self, image_path):
        new_node = Node(image_path)
        if self.head is None:
            self.head = new_node
            self.current = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    
    #displaying the image 
    def display_image(self):
        if self.current != None:
            print("Currently viewing:", self.current.data)
        else:
            print("No image to display.")
    
    #traversing to the next image
    def next_image(self):
        if self.current and self.current.next != None:
            self.current = self.current.next
            print("Moving to next image.")
            self.display_image()
        else:
            print("No next image available.")
    
    #traversing to the previous image
    def prev_image(self):
        if self.current == self.head:
            print("No previous image available.")
        else:
            prev_node = self.head
            while prev_node.next != self.current:
                prev_node = prev_node.next
            self.current = prev_node
            print("Moving to previous image.")
            self.display_image()
    
    #deleting the current image
    def delete_image(self):
        if self.current == self.head:
            self.head = self.head.next
            self.current = self.head
            print("Deleted current image.")
        else:
            prev_node = self.head
            while prev_node.next != self.current:
                prev_node = prev_node.next
            prev_node.next = self.current.next
            self.current = prev_node.next
            print("Deleted current image.")


view = ImageViewer()
view.add_image("image1.jpg")
view.add_image("image2.jpg")
view.add_image("image3.jpg")

view.display_image()  # Display the first image
view.next_image()    # Display the next image
view.next_image()    # Display the next image
view.prev_image()     # Display the previous image
view.delete_image()   # Delete the current image
view.display_image()  # Display the current image
