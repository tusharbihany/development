//
//  ViewController.h
//  Calculator
//
//  Created by Bihany, Tushar on 1/12/17.
//  Copyright © 2017 Bihany, Tushar. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface ViewController : NSViewController
{
    NSString *operand1;
    NSString *operand2;
    NSString *inputstring;
    NSString *operation;

    __weak IBOutlet NSButton *digits;
    
    __weak IBOutlet NSTextField *result;

}

-(IBAction)digits:(NSButton *)sender;


@end
