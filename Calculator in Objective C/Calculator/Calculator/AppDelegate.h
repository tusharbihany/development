//
//  AppDelegate.h
//  Calculator
//
//  Created by Bihany, Tushar on 1/12/17.
//  Copyright © 2017 Bihany, Tushar. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#include "ViewController.h"

@interface AppDelegate : NSObject <NSApplicationDelegate>
{
    ViewController *viewController;
}
@property (readonly, strong, nonatomic) NSPersistentStoreCoordinator *persistentStoreCoordinator;
@property (readonly, strong, nonatomic) NSManagedObjectModel *managedObjectModel;
@property (readonly, strong, nonatomic) NSManagedObjectContext *managedObjectContext;


@end

